function SourceCard({
    Chunk,
    Relevance,
    Text,
}) {
    return (
        <div className="SourceCard">
            <div className="PdfIcon small">PDF</div>

            <div>
                <strong>AWS Cloud Practitioner.pdf</strong>
                <span>
                    {Chunk} · Relevance: {Relevance}
                </span>
            </div>
            <p>{Text}</p>
        </div>
    );
}

export default SourceCard;